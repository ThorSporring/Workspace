using Ex3;
using Microsoft.EntityFrameworkCore;

public class CFG()
{
    private static void Main()
    {
        using var db = new MyDbContext();
        
        
        
        
    }

    private static void SeedDb(MyDbContext context)
    {
        // Seed Cars
        for (int i = 0; i < 10; i++)
        {
            var car = new Car
            {
                Brand = $"Brand{i}",
                ProductionYear = 2020 + i
            };

            context.Cars.Add(car);
        }

        // Seed Persons
        for (int i = 0; i < 10; i++)
        {
            var person = new Person
            {
                FirstName = $"FirstName{i}",
                LastName = $"LastName{i}",
                Adress = $"Address{i}",
                Car = context.Cars.Find(i + 1) // Assuming CarId is 1-based
            };

            context.Persons.Add(person);
        }

        // Save changes to the database
        context.SaveChanges();
    }
    
}