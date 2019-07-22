
from questionnaire.models import Questionnaire
from .configuration import Configuration
class ConfigurationBuilder(Configuration):

    """
        Permit to create serializable uninitialized configuration easily.
        We just use the default dict for a Builder, the user will be able to
        modify value from the default.

        We delete unwanted questionnaire in self._conf in order to print
        only what the user want.
    """

    def __init__(self, questionnaire=None):
        """ Initialize a configuration file.

        :param questionnaire questionnaire: If questionnaire is defined we generate configuration
        only for this questionnaire."""
        super(ConfigurationBuilder, self).__init__(self.DEFAULT_PATH)
        self._init_default()
        if questionnaire:
            for other_questionnaire in Questionnaire.objects.all():
                unwanted_questionnaire = questionnaire.name != other_questionnaire.name
                if unwanted_questionnaire:
                    del self._conf[other_questionnaire.name]

    def _init_default(self):
        """ Return the default configuration. """
        default_value_generic = self._conf["generic"]
        default_value_chart = self._conf["generic"]["chart"]
        default_values = {"chart": default_value_chart}
        for questionnaire in Questionnaire.objects.all():
            if self._conf.get(questionnaire.name) is None:
                self._conf[questionnaire.name] = default_value_generic
            categories = {}
            for category in questionnaire.categories.all():
                categories[category.name] = default_values
            self._conf[questionnaire.name]["categories"] = categories
            questions = {}
            for question in questionnaire.questions.all():
                questions[question.text] = default_values
            self._conf[questionnaire.name]["questions"] = questions
