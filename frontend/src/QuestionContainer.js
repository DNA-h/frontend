import React, { Component } from 'react';

class QuestionContainer extends Component {
    constructor() {
        super();
        this.state = {
            answerVisibility: false,
            answerDisplay: false,
            answerDecline: false
        }
    }

    showAnswer = () => {
        this.setState({
            answerVisibility: true
        })
    }
    displayAnswer = () => {
        this.setState({
            answerDisplay: true
        })
    }
    declineAnswer = () => {
        this.setState({
            answerDecline: true
        })
    }

    render() {
        const { questionMessage, questionAnswer } = this.props
        return (
            <>{!this.state.answerDecline ?
                <div>
                    {!this.state.answerVisibility ?
                        <div className="container">
                            <p className="question">{questionMessage}</p>
                            <div className="btn btn-primary show-answer" onClick={this.showAnswer}>Show Answer</div>
                        </div>
                        :
                        <>
                            {!this.state.answerDisplay ?
                                <div className="container">
                                    <div className="alert alert-info">
                                        <p>Reveal the answer?</p>
                                        <div className="btn-primary" onClick={this.displayAnswer}>Yes Please</div>
                                        <div className="btn-danger" onClick={this.declineAnswer}>Not Yet</div>
                                    </div>
                                    <p className="question">{questionMessage}</p>
                                    <div className="btn btn-primary show-answer">Show Answer</div>
                                </div>
                                :
                                <div className="container">
                                    <p className="question">{questionMessage}</p>
                                    <button className="btn btn-primary show-answer" disabled>Show Answer</button>
                                    <p className="answer">{questionAnswer}</p>
                                </div>
                            }
                        </>
                    }
                </div>
                :
                <div className="container">
                    <p className="question">{questionMessage}</p>
                    <div className="btn btn-primary show-answer" onClick={this.showAnswer}>Show Answer</div>
                </div>
            }
            </>
        );
    }
}





export default QuestionContainer;