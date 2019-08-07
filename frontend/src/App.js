import React from 'react';
import Notification from './Notification';
import QuestionList from './QuestionList';


function App() {
  let notification = {
    message: "Hello world",
    type: "error"
  };

  let questions = 
     [{
      question: 'What is the average the airspeed velocity of a (European) unladen swallow?',
      answer: '11 meters per second'
    },
    {
      question: 'What are the first 10 digits of PI?',
      answer: '3.141592653'
    },
    {
      question: 'What is your preferred javascript framework?',
      answer: 'React'
    }

    ]
  

  return (
    <div id="app">
      <Notification notificationMessage={notification} />
      <QuestionList questions={questions}/>
    </div>
  )
}





export default App;