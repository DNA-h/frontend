import React from 'react';
import QuestionContainer from './QuestionContainer';

const QuestionList = ({questions}) => {
    const questionArray = Object.keys(questions).map((list,i) =>
        <QuestionContainer 
            key={i}
            questionMessage={questions[list].question_text}
            question_type={questions[list].question_type}
            question_choices={questions[list].question_choices}
        />
    );
    return (
        <div>
            {questionArray}
        </div>
    )
};

export default QuestionList;
