// ATTEMPT 1 - First instinct: just check if divisible by 7
// Forgot the second condition entirely (contains digit 7)

const isLucky = (x) => {
    return x % 7 === 0;
};

module.exports = { isLucky };
