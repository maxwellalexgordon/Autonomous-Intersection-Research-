// Auto-generated. Do not edit!

// (in-package intersection.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class CarComOneRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.inOut = null;
      this.vin = null;
      this.speed = null;
      this.accel = null;
      this.enterTime = null;
      this.lane = null;
      this.turn = null;
      this.length = null;
      this.width = null;
    }
    else {
      if (initObj.hasOwnProperty('inOut')) {
        this.inOut = initObj.inOut
      }
      else {
        this.inOut = 0;
      }
      if (initObj.hasOwnProperty('vin')) {
        this.vin = initObj.vin
      }
      else {
        this.vin = 0;
      }
      if (initObj.hasOwnProperty('speed')) {
        this.speed = initObj.speed
      }
      else {
        this.speed = 0.0;
      }
      if (initObj.hasOwnProperty('accel')) {
        this.accel = initObj.accel
      }
      else {
        this.accel = 0.0;
      }
      if (initObj.hasOwnProperty('enterTime')) {
        this.enterTime = initObj.enterTime
      }
      else {
        this.enterTime = 0;
      }
      if (initObj.hasOwnProperty('lane')) {
        this.lane = initObj.lane
      }
      else {
        this.lane = 0;
      }
      if (initObj.hasOwnProperty('turn')) {
        this.turn = initObj.turn
      }
      else {
        this.turn = 0;
      }
      if (initObj.hasOwnProperty('length')) {
        this.length = initObj.length
      }
      else {
        this.length = 0.0;
      }
      if (initObj.hasOwnProperty('width')) {
        this.width = initObj.width
      }
      else {
        this.width = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CarComOneRequest
    // Serialize message field [inOut]
    bufferOffset = _serializer.int64(obj.inOut, buffer, bufferOffset);
    // Serialize message field [vin]
    bufferOffset = _serializer.int64(obj.vin, buffer, bufferOffset);
    // Serialize message field [speed]
    bufferOffset = _serializer.float64(obj.speed, buffer, bufferOffset);
    // Serialize message field [accel]
    bufferOffset = _serializer.float64(obj.accel, buffer, bufferOffset);
    // Serialize message field [enterTime]
    bufferOffset = _serializer.int64(obj.enterTime, buffer, bufferOffset);
    // Serialize message field [lane]
    bufferOffset = _serializer.int64(obj.lane, buffer, bufferOffset);
    // Serialize message field [turn]
    bufferOffset = _serializer.int64(obj.turn, buffer, bufferOffset);
    // Serialize message field [length]
    bufferOffset = _serializer.float64(obj.length, buffer, bufferOffset);
    // Serialize message field [width]
    bufferOffset = _serializer.float64(obj.width, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CarComOneRequest
    let len;
    let data = new CarComOneRequest(null);
    // Deserialize message field [inOut]
    data.inOut = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [vin]
    data.vin = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [speed]
    data.speed = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [accel]
    data.accel = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [enterTime]
    data.enterTime = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [lane]
    data.lane = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [turn]
    data.turn = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [length]
    data.length = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [width]
    data.width = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 72;
  }

  static datatype() {
    // Returns string type for a service object
    return 'intersection/CarComOneRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2642c81ca61d90ff57b0dfdde379e953';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 inOut
    int64 vin
    float64 speed
    float64 accel
    int64 enterTime
    int64 lane
    int64 turn
    float64 length
    float64 width
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CarComOneRequest(null);
    if (msg.inOut !== undefined) {
      resolved.inOut = msg.inOut;
    }
    else {
      resolved.inOut = 0
    }

    if (msg.vin !== undefined) {
      resolved.vin = msg.vin;
    }
    else {
      resolved.vin = 0
    }

    if (msg.speed !== undefined) {
      resolved.speed = msg.speed;
    }
    else {
      resolved.speed = 0.0
    }

    if (msg.accel !== undefined) {
      resolved.accel = msg.accel;
    }
    else {
      resolved.accel = 0.0
    }

    if (msg.enterTime !== undefined) {
      resolved.enterTime = msg.enterTime;
    }
    else {
      resolved.enterTime = 0
    }

    if (msg.lane !== undefined) {
      resolved.lane = msg.lane;
    }
    else {
      resolved.lane = 0
    }

    if (msg.turn !== undefined) {
      resolved.turn = msg.turn;
    }
    else {
      resolved.turn = 0
    }

    if (msg.length !== undefined) {
      resolved.length = msg.length;
    }
    else {
      resolved.length = 0.0
    }

    if (msg.width !== undefined) {
      resolved.width = msg.width;
    }
    else {
      resolved.width = 0.0
    }

    return resolved;
    }
};

class CarComOneResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.requestedAccel = null;
      this.expectedTime = null;
    }
    else {
      if (initObj.hasOwnProperty('requestedAccel')) {
        this.requestedAccel = initObj.requestedAccel
      }
      else {
        this.requestedAccel = 0;
      }
      if (initObj.hasOwnProperty('expectedTime')) {
        this.expectedTime = initObj.expectedTime
      }
      else {
        this.expectedTime = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CarComOneResponse
    // Serialize message field [requestedAccel]
    bufferOffset = _serializer.int64(obj.requestedAccel, buffer, bufferOffset);
    // Serialize message field [expectedTime]
    bufferOffset = _serializer.int64(obj.expectedTime, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CarComOneResponse
    let len;
    let data = new CarComOneResponse(null);
    // Deserialize message field [requestedAccel]
    data.requestedAccel = _deserializer.int64(buffer, bufferOffset);
    // Deserialize message field [expectedTime]
    data.expectedTime = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'intersection/CarComOneResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e753458bdfec6c28c64ea4577fe4d8cc';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 requestedAccel
    int64 expectedTime
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CarComOneResponse(null);
    if (msg.requestedAccel !== undefined) {
      resolved.requestedAccel = msg.requestedAccel;
    }
    else {
      resolved.requestedAccel = 0
    }

    if (msg.expectedTime !== undefined) {
      resolved.expectedTime = msg.expectedTime;
    }
    else {
      resolved.expectedTime = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: CarComOneRequest,
  Response: CarComOneResponse,
  md5sum() { return '270abad34ce1b23dffdbb99ceeeccc24'; },
  datatype() { return 'intersection/CarComOne'; }
};