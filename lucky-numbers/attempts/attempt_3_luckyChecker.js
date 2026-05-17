// ATTEMPT 3 - Converted to string first (good!), but used indexOf > 0 instead of >= 0
// Bug: numbers whose FIRST digit is 7 (like 71, 72, 73...) have indexOf('7') === 0
// 0 > 0 is false, so they are missed!
// Example: 71 -- 71 % 7 = 1 (not divisible), indexOf('7') = 0, 0 > 0 = false --> NOT lucky
// But 71 CONTAINS a 7, so it SHOULD be lucky!

const isLucky = (x) => {
    return x % 7 === 0 || String(x).indexOf('7') > 0;
};

module.exports = { isLucky };
