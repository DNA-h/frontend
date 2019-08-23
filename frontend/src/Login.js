import React from 'react';
import "./MyFont.css";

export default class Login extends React.Component {
  render() {
    return (
      <div
        style={{
          display:'flex',
          alignItems:'center',
          flexDirection:'column',
          justifyContent:'center',
          height:window.innerHeight
        }}
      >
        <p
          className={'custom_bold'}
          style={{
            height:'10%',
            fontSize:30
          }}
        >
          ماهیمو
        </p>
        <div
          style={{
            borderWidth: 1,
            borderColor: '#d9d9d9',
            borderStyle: 'solid',
            height:'50%',
            display:'flex',
            flexDirection:'column',
            alignItems:'flex-end',
            paddingRight:20,
            paddingLeft:20,
          }}
        >
          <p
            className={'custom_bold'}
            style={{
              alignSelf:'center',
              fontSize:24
            }}
          >
            ورود به ماهیمو
          </p>
          <p
            className={'custom_font'}
          >
            نام کاربری
          </p>
          <input
            className={'custom_font'}
            style={{
              borderRadius:4,
              borderWidth:1,
              borderColor:'#CCC',
              borderStyle:'solid',
              width:'100%'
            }}
            type={'text'}
          />
          <p
            className={'custom_font'}
          >
            رمز عبور
          </p>
          <input
            className={'custom_font'}
            style={{
              borderRadius:4,
              borderWidth:1,
              borderColor:'#CCC',
              borderStyle:'solid',
              width:'100%'
            }}
            type={'text'}
          />
          <div
            style={{
              display:'flex',
              flexDirection:'row'
            }}
          >
            <a
              href={"#"}
              className={'custom_font'}
            >
              رمز عبور خود را فراموش کرده اید؟
            </a>
          <label
            className={'custom_font'}
          >
            مرا به خاطر بسپار
            <input
              className={'custom_font'}
              style={{
                borderRadius:4,
                borderWidth:1,
                borderColor:'#CCC',
                borderStyle:'solid',
              }}
              type={'checkbox'}
            />
          </label>
          </div>
          <p
            className={'custom_font'}
            style={{
              backgroundColor:'#0094b5',
              width:'100%',
              textAlign:'center',
              paddingBottom:5
            }}
          >
            ورود
          </p>
        </div>
      </div>
    );
  }
}