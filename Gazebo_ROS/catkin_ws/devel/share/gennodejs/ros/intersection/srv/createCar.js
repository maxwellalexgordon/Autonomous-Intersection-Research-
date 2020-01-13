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

class createCarRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.check = null;
    }
    else {
      if (initObj.hasOwnProperty('check')) {
        this.check = initObj.check
      }
      else {
        this.check = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type createCarRequest
    // Serialize message field [check]
    bufferOffset = _serializer.int64(obj.check, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type createCarRequest
    let len;
    let data = new createCarRequest(null);
    // Deserialize message field [check]
    data.check = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'intersection/createCarRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'cd2b440b511ca1d8964b537e735641de';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 check
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new createCarRequest(null);
    if (msg.check !== undefined) {
      resolved.check = msg.check;
    }
    else {
      resolved.check = 0
    }

    return resolved;
    }
};

class createCarResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
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
    // Serializes a message object of type createCarResponse
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
    //deserializes a message object of type createCarResponse
    let len;
    let data = new createCarResponse(null);
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
    return 64;
  }

  static datatype() {
    // Returns string type for a service object
    return 'intersection/createCarResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '17376b3fc48c1885fb019580792ccc11';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    const resolved = new createCarResponse(null);
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

module.exports = {
  Request: createCarRequest,
  Response: createCarResponse,
  md5sum() { return '81fafe211a05479f18572c2a83d88d33'; },
  datatype() { return 'intersection/createCar'; }
};
