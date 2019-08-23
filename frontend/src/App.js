import React from 'react';
import Notification from './Notification';
import QuestionList from './QuestionList';


class App extends React.Component {

  constructor(props) {
    super(props);
    this.notification = {
      message: undefined,
      type: "error",
    };
    this.state ={
      questions:[]
    }
  }

  async componentDidMount() {
    fetch("http://127.0.0.1:8000/q/1/").then((res) =>
      res.json().then((result) => this.setState({questions:result}))
    )
  }

  render() {
    return (
      <div id="app">
        <Notification notificationMessage={this.notification}/>
        <QuestionList questions={this.state.questions}/>
      </div>
    )
  }
}


export default App;