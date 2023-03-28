#!/usr/bin/node

exports.esrever = function (list) {
  const newArray = [];
  for (const element of list) {
    newArray.unshift(element);
  }
  return newArray;
};
