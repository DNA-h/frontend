import logging
from django.utils import translation
from questionnaire.exporter.csv import Questionnaire2Csv
from questionnaire.exporter.tex.configuration import Configuration
from questionnaire.exporter.tex.questionnaire2tex import Questionnaire2Tex
from django import template
from sys import version_info
from django.core.management.base import BaseCommand
from questionnaire.exporter.tex import ConfigurationBuilder
from questionnaire.models import Question, Questionnaire

LOGGER = logging.getLogger(__name__)

class QuestionnaireCommand(BaseCommand):

    requires_system_checks = False

    def add_arguments(self, parser):
        help_text = "The {}s of the {}s we want to generate. Default is None."
        parser.add_argument(
            "--questionnaire-all",
            action="store_true",
            help="Use to " "generate all questionnaires. Default is False.",
        )
        parser.add_argument(
            "--questionnaire-id",
            nargs="+",
            type=int,
            help=help_text.format("primary key", "questionnaire"),
        )
        parser.add_argument(
            "--questionnaire-name",
            nargs="+",
            type=str,
            help=help_text.format("name", "questionnaire"),
        )
        parser.add_argument(
            "--question-all",
            action="store_true",
            help="Use to" " generate all questions. Default is False.",
        )
        parser.add_argument(
            "--question-id",
            nargs="+",
            type=int,
            help=help_text.format("primary key", "question"),
        )
        parser.add_argument(
            "--question-text",
            nargs="+",
            type=str,
            help=help_text.format("text", "question"),
        )

    def raise_value_error(self, error_type, value):
        """ Raise a ValueError with a clean error message in python 2.7 and 3.

        :param string value: the attempted value. """
        if error_type in ["question-id", "question-text"]:
            base = "--question-id {} / --question-text '{}'\n"
            valids = [(q.pk, q.text) for q in Question.objects.all()]
        elif error_type in ["questionnaire-name", "questionnaire-id"]:
            base = "--questionnaire-id {} / --questionnaire-name '{}'\n"
            valids = [(s.pk, s.name) for s in Questionnaire.objects.all()]
        msg = "You tried to get --{} '{}' ".format(error_type, value)
        if valids:
            msg += "but is does not exists. Possibles values :\n"
            for pk, name in valids:
                msg += base.format(pk, name)
            msg = msg[:-1]  # Remove last \n
        else:
            msg += "but there is nothing in the database."
        # Compatibility for python 2.7 and 3
        # See: https://stackoverflow.com/questions/46076279/
        if version_info.major == 2:  # pragma: no cover
            raise ValueError(msg.encode("utf-8"))
        else:  # pragma: no cover
            raise ValueError(msg)

    def check_mutually_exclusive(self, opts):
        """ We could use the ArgParse option for this, but the case is
        simple enough to be treated this way. """
        prefix = "You cannot generate only some "
        postfix = " to generate everything. Use one or the other."
        all_questions = opts.get("question_all")
        some_questions = opts.get("question_text") or opts.get("question_id")
        all_questionnaires = opts.get("questionnaire_all")
        some_questionnaires = opts.get("questionnaire_name") or opts.get("questionnaire_id")
        if all_questions and some_questions:
            exit(
                prefix + "questions with '--question-id' or --question-text' "
                "while also using '--question-all'" + postfix
            )
        if all_questionnaires and some_questionnaires:
            exit(
                prefix + "questionnaire with '--questionnaire-id' or '--questionnaire-name' "
                "while also using '--questionnaire-all'" + postfix
            )

    def check_nothing_at_all(self, options):
        at_least_a_question = (
            options.get("question_all")
            or options.get("question_text")
            or options.get("question_id")
        )
        at_least_a_questionnaire = (
            options.get("questionnaire_all")
            or options.get("questionnaire_name")
            or options.get("questionnaire_id")
        )
        if not at_least_a_question and not at_least_a_questionnaire:
            exit(
                "Nothing to do, add at least one of the following options :\n"
                "'--question-id', '--question-text' '--question-all',"
                "'--questionnaire-id', '--questionnaire-name', '--questionnaire-all'."
            )

    def handle(self, *args, **options):
        self.check_mutually_exclusive(options)
        self.check_nothing_at_all(options)
        if options.get("question_all"):
            self.questions = Question.objects.all()
        else:
            self.questions = []
            if options.get("question_text"):
                for question_text in options["question_text"]:
                    try:
                        self.questions.append(Question.objects.get(text=question_text))
                    except Question.DoesNotExist:
                        self.raise_value_error("question-text", question_text)
            if options.get("question_id"):
                for question_id in options["question_id"]:
                    try:
                        self.questions.append(Question.objects.get(pk=question_id))
                    except Question.DoesNotExist:
                        self.raise_value_error("question-id", question_id)
        if options.get("questionnaire_all"):
            self.questionnaires = Questionnaire.objects.all()
        else:
            self.questionnaires = []
            if options.get("questionnaire_name"):
                for questionnaire_name in options["questionnaire_name"]:
                    try:
                        self.questionnaires.append(Questionnaire.objects.get(name=questionnaire_name))
                    except Questionnaire.DoesNotExist:
                        self.raise_value_error("questionnaire-name", questionnaire_name)
            if options.get("questionnaire"):
                for questionnaire in options["questionnaire"]:
                    try:
                        self.questionnaires.append(Questionnaire.objects.get(pk=questionnaire))
                    except Questionnaire.DoesNotExist:
                        self.raise_value_error("questionnaire-id", questionnaire)




class Commandex(QuestionnaireCommand):

    """
        See the "help" var.
    """

    help = """This command permit to export all questionnaire in the database as csv
               and tex."""

    def add_arguments(self, parser):
        super(Commandex, self).add_arguments(parser)
        parser.add_argument(
            "--configuration-file",
            "-c",
            type=str,
            help="Path to the tex configuration file.",
        )
        parser.add_argument(
            "--force",
            "-f",
            action="store_true",
            help="Force the generation, "
            "even if the file already exists. Default is False.",
        )
        parser.add_argument(
            "--csv", action="store_true", help="Export as csv. Default is False."
        )
        parser.add_argument(
            "--tex", action="store_true", help="Export as tex. Default is False."
        )
        parser.add_argument(
            "--pdf",
            action="store_true",
            help="Equivalent to --tex but we will also try to compile the pdf.",
        )
        parser.add_argument(
            "--language",
            help="Permit to change the language used for "
            "generation (default is defined in the settings).",
        )

    def check_nothing_at_all(self, options):
        QuestionnaireCommand.check_nothing_at_all(self, options)
        if not options["csv"] and not options["tex"] and not options["pdf"]:
            exit("Nothing to do : add option --tex or --pdf, --csv,  or both.")

    def handle(self, *args, **options):
        super(Commandex, self).handle(*args, **options)
        translation.activate(options.get("language"))
        for questionnaire in self.questionnaires:
            LOGGER.info("Generating results for '%s'", questionnaire)
            exporters = []
            if options["csv"]:
                exporters.append(Questionnaire2Csv(questionnaire))
            if options["tex"] or options["pdf"]:
                configuration_file = options.get("configuration_file")
                if configuration_file is None:
                    msg = "No configuration file given, using default values."
                    LOGGER.warning(msg)
                configuration = Configuration(configuration_file)
                exporters.append(Questionnaire2Tex(questionnaire, configuration))
            for exporter in exporters:
                if options["force"] or exporter.need_update():
                    exporter.generate_file()
                    if options["pdf"] and type(exporter) is Questionnaire2Tex:
                        exporter.generate_pdf()
                else:
                    LOGGER.info(
                        "\t- %s's %s were already generated use the "
                        "--force (-f) option to generate anyway.",
                        questionnaire,
                        exporter._get_X(),
                    )


class Commandgen(QuestionnaireCommand):

    """
        See the "help" var.
    """

    help = """This command permit to generate the latex configuration in order
    to manage the questionnaire report generation. """

    def add_arguments(self, parser):
        super(Commandgen, self).add_arguments(parser)
        parser.add_argument("output", nargs="+", type=str, help="Output prefix.")

    def write_conf(self, name, conf):
        file_ = open(name, "w", encoding="UTF-8")
        file_.write(str(conf))
        file_.close()

    def handle(self, *args, **options):
        super(Commandgen, self).handle(*args, **options)
        output = options["output"]
        if len(output) != len(self.questionnaires):
            exit(
                "You want to generate {} questionnaires ".format(len(self.questionnaires))
                + "but you only gave {} output names".format(len(output))
            )
        for i, questionnaire in enumerate(self.questionnaires):
            conf = ConfigurationBuilder(questionnaire)
            self.write_conf(output[i], conf)

# -*- coding: utf-8 -*-


