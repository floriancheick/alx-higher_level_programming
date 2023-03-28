#!/usr/bin/node

exports.logMe = function (item) {
  console.log(`${exports.logMe.count}: ${item}`);
  exports.logMe.count++;
};

exports.logMe.count = 0;
