const isLucky = (x) => {
    return x % 7 === 0 || x.toString().includes('7');
};

module.exports = { isLucky };
