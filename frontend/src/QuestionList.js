import React from 'react';
import QuestionContainer from './QuestionContainer';

const QuestionList = ({questions}) => {
    const questionArray = questions.map((list,i) => 
        <QuestionContainer 
            key={i}
            questionMessage={list.question}
            questionAnswer={list.answer}
        />
    )
    return (
        <div>
            {questionArray}
        </div>
    )
}

export default QuestionList;
