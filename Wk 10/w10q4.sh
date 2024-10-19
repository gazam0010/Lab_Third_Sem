# Perform basic arithmetic operations

echo "Enter first number: "
read first_num
echo "Enter second number: "
read second_num

sum=$((first_num+second_num))
echo "Addition: $sum"

sub=$((first_num-second_num))
echo "Subtraction: $sub"

prod=$((first_num*second_num))
echo "Product: $prod"

if [[ $first_num -ne 0 && $second_num -ne 0 ]]; then
    div=$((first_num / second_num))
    echo "Division: $div"
else
    echo "Division: Cannot divide by zero"
fi