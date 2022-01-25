// Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
// For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
// Bonus: Can you do this in one pass?


var k = 17;
var l = [10, 15, 3, 7];
for (let i = 0; i < l.length; ++i) {
    for (let j = 1; j < l.length - i; ++j) {
        const element = l[i + j] + l[i]
        if (element == k) {
            console.log("true")
            break
        }
    }
};
// This would take O(N^2) because of nested loops. even though the second loop is not repeating the entire search each time.
