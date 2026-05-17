// ATTEMPT 4 - Final fix: use .includes() on the string, not the number
// OR use indexOf >= 0 instead of > 0
// Both work. .includes() is cleaner and easier to read.

const isLucky = (x) => {
    return x % 7 === 0 || x.toString().includes('7');
};

module.exports = { isLucky };
