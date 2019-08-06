import React, {Component} from 'react';


class Confirmation extends Component {

    render(){
        const {accept, decline, visibility, hideConfirmation} = this.props;
        return (
            <>
                {visibility ?
                    <div className="alert alert-info">
                        <p>{this.props.message}</p>
                        <div className="btn btn-primary" onClick={() => { accept(); hideConfirmation(); }}>Sure</div>
                        <div className="btn btn-danger" onClick={() => { decline(); hideConfirmation(); }}>No Thanks</div>
                    </div>
                    :
                    null
                }
            </>
        )
}

}


export default Confirmation;


