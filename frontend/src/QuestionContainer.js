import React, {Component} from 'react';

class QuestionContainer extends Component {

  renderType() {
    if (this.props.question_type === "text") {
      return (
        <div>
          <input type={'textarea'}
          />
        </div>
      )
    } else if (this.props.question_type === "radio") {
      const options = this.props.question_choices.split(",");
      const optionArray = options.map((list, index) =>
        <div key={list}>
          <label>{list}</label>
          <input type={'radio'}
          />
        </div>
      );
      return (
        optionArray
      )
    }else if (this.props.question_type === "select-multiple") {
      const options = this.props.question_choices.split(",");
      const optionArray = options.map((list, index) =>
        <div key={list}>
          <label>{list}</label>
          <input type={'checkbox'}
          />
        </div>
      );
      return (
        optionArray
      )
    }
  }

  render() {
    const {questionMessage} = this.props;
    return (
      <>
        <div className="container">
          <p className="question">{questionMessage}</p>
          {this.renderType()}
          <div className="btn btn-primary show-answer" onClick={this.showAnswer}>Send Answer</div>
        </div>
      </>
    );
  }
}


export default QuestionContainer;