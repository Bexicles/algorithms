function answer = karatsuba(x, y)
% Takes two n-digit numbers and splits them into two halves (called A, B for the first number and then C, D for the second)
% It then calculates 1) A*C, 2) B*D and 3) (A+B)*(C+D)
% It then subtracts 2) and 1) from 3) to make 4)
% The answer is then the sum of 1) padded with n zeros, 2), and 4) padded with n/2 zeros.
% The algorithm will call itself recursively at any stage that it is trying to multiply two numbers that have more than one digit each.

fprintf('Running karatsuba for ... %d \n', x, y);

% Converts input integers into strings, so can more easily split in two
x_str = num2str(x);
y_str = num2str(y);

% Calculates length of each string
n1 = length(x_str);
n2 = length(y_str);

% Tests lengths of n1 & n2 to see if odd, if so adds leading zero to each string

zero = num2str(0); % creating a string with a zero

if mod(n1,2) ~=0
  x_str = strcat(zero, x_str);
  n1 = length(x_str);
  end
  
if mod(n2,2) ~=0
  y_str = strcat(zero, y_str);
  n2 = length(y_str);
  end


% Splits first string into two (A, B) and converts them back to numbers
% Also stores length of A & B in variables to be used later


A = x_str(1:n1/2);
A_len = length(A);
A = str2double(A)

B = x_str((n1/2)+1:n1);
B_len = length(B);
B = str2double(B)

% Splits first string into two (C, D) and converts them back to numbers
% Also stores length of A & B in variables to be used later
C = y_str(1:n1/2);
C_len = length(C);
C = str2double(C)

D = y_str((n1/2)+1:n1);
D_len = length(D);
D = str2double(D)

% Tests if length of A or B is longer than 1, if so calls Karatsuba
% Else, calculates AC
if A_len > 1
  AC = karatsuba(A, C);
  
else
  AC = A*C;
  end

% Tests if length of C or D is longer than 1, if so calls Karatsuba
% Else, calculates BD
if B_len > 1
  BD = karatsuba(B, D);
else
  BD = B*D;
  end

% Calculates (A+B) and (C+D)
AplusB = A + B;
CplusD = C + D;

% Tests if (A+B) is is longer than 1, if so calls Karatsuba
% Else, calculates (A+B)*(C+D)

if length(AplusB) > 1
  temp = karatsuba(AplusB, CplusD);
else
  temp = (AplusB) * (CplusD);
  end

% Calculates temp - BD - AC
temp2 = temp - BD - AC;

% Appends n zeros to AC & temp2
AC_zeros = AC * 10^n1;
temp2_zeros = temp2 * 10^(n1/2);

% Adds AC_zeros, BD and temp2_zeros to get final answer
answer = AC_zeros + temp2_zeros + BD;

endfunction
