// ATTEMPT 2 - Remembered the digit check, but called .includes() on a NUMBER
// JavaScript numbers don't have .includes() -- this crashes with:
// TypeError: x.includes is not a function

const isLucky = (x) => {
    return x % 7 === 0 || x.includes('7');
};

module.exports = { isLucky };
