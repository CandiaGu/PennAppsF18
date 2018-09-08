import React from 'react';
import { Text, View, TouchableOpacity } from 'react-native';
import { Camera, Permissions, FileSystem } from 'expo';

export default class CameraExample extends React.Component {


  state = {
    hasCameraPermission: null,
    type: Camera.Constants.Type.back,
    whiteBalance: Camera.Constants.WhiteBalance.fluorescent,
    tmp: 'not taken',
    newPhotos: "false",
    uri: "none",
    base64: null,
    ratio: "16:9",
    flashMode: Camera.Constants.FlashMode.off
    };



  componentDidMount() {
    this.interval = setInterval(() => this.takePicture(), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.interval);
  }

  async componentWillMount() {
    const { status } = await Permissions.askAsync(Permissions.CAMERA);
    this.setState({ hasCameraPermission: status === 'granted' });
  }


  takePicture = () => {
    // try {
    //   if (this.camera) {
    //       //
    try{
      let photo = this.camera.takePictureAsync({base64:true}).then(data => {
      console.log(data.base64);
      fetch('https://mywebsite.com/endpoint/', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          base64: data.base64
        }),
      });
        console.log("sending img")
    });
      
    }
    catch(error){
      console.error(error);
    }

    console.log("hello");
    
  }

  sendIMG = (base64) => {
    fetch('https://mywebsite.com/endpoint/', {
    method: 'POST',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      base64: base64
    }),
  })
  .catch((error) =>{
    console.error(error);
  });
    console.log("sending img")
  }

  

  render() {
    const { hasCameraPermission } = this.state;
    if (hasCameraPermission === null) {
      return <View />;
    } else if (hasCameraPermission === false) {
      return <Text>No access to camera</Text>;
    } else {
      return (
        <View style={{ flex: 1 }}>
          <Camera style={{ flex: 1 }} 
          type={this.state.type}
          ref={ref => {
            this.camera = ref;
          }}
          ratio={this.state.ratio}
          flashMode = {this.state.flashMode}
          >
            <View
              style={{
                flex: 1,
                backgroundColor: 'transparent',
                flexDirection: 'row',
              }}>
              <TouchableOpacity
                style={{
                  flex: 0.2,
                  alignSelf: 'flex-end',
                  alignItems: 'center',
                }}
                onPress={this.takePicture}>
                <Text
                  style={{ fontSize: 18, marginBottom: 10, color: 'white' }}>
                  {this.state.tmp}
                </Text>

              </TouchableOpacity>
              <TouchableOpacity
                style={{
                  flex: 0.2,
                  alignSelf: 'flex-end',
                  alignItems: 'center',
                }}>
                <Text
                  style={{ fontSize: 18, marginBottom: 10, color: 'white' }}>
                  {this.state.uri}
                </Text>

              </TouchableOpacity>
            </View>
          </Camera>
        </View>
      );
    }
  }
}