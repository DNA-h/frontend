import React, {Component} from 'react';
import Confirmation from './Confirmation';



class Notification extends Component {
    constructor(props) {
        super(props)
        this.state = {
            message: 'Should we bake a pie?',
            type: 'message',
            visibility: true
        }
    }

    hideConfirmation = () => {
        this.setState({
            visibility: false
        });
    }

    accept = () => {
        this.setState({
            visibility: true
        });
    }

    decline = () => {
        this.setState({
            visibility: false
        });
    }
    render() {
        const { notificationMessage } = this.props;
        return (
            <div>
                {!notificationMessage.message ?
                    <div id="app"></div>
                    :
                    <div id="app">
                        {!notificationMessage.type ?
                            <div className='alert alert-info'>
                                {notificationMessage.message}
                            </div>
                            :
                            <div className='alert alert-danger'>
                                {notificationMessage.message}
                            </div>
                        }
                    </div>
                }
                <Confirmation
                    message={this.state.message}
                    accept={this.accept}
                    decline={this.decline}
                    hideConfirmation={this.hideConfirmation}
                    visibility={this.state.visibility}
                />
            </div>

        )
    }
}


export default Notification;