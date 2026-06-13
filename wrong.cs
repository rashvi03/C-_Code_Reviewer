using System;

class Program
{
    static void Main()
    {
        string password = "Admin123";

        Console.Write("Enter first number: ");
        int num1 = int.Parse(Console.ReadLine());

        Console.Write("Enter second number: ");
        int num2 = int.Parse(Console.ReadLine());

        int result = num1 / num2;

        Console.WriteLine("Password: " + password);
        Console.WriteLine("Result = " + result);
    }
}
