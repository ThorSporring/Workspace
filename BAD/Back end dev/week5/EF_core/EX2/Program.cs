


using EX2;
using Microsoft.EntityFrameworkCore;

public class CFG()
{
    private static void Main()
    {
        using var db = new MyDbContext();
        
        SeedDb(db);
        ListAllPcs(db);
        
        
    }

    private static void ListAllPcs(MyDbContext db)
    {
        foreach (var pc in db.Pcs.Include(p => p.Product).ToList())
        {
            System.Console.WriteLine(pc);
        }
    }
    private static void SeedDb(MyDbContext db)
    {
        Product thinkpadT560 = new Product()
        {
            Maker = "Thinkpad",
            Model = "T560",
            Type = "Laptop"
        };

        db.Products.Add(thinkpadT560);
        Laptop laptop1 = new Laptop()
        {
            Product = thinkpadT560,
            Price = 23,
            Speed = 34,
            Ram = 16,
        };
        db.Laptops.Add(laptop1);

        Product hp123 = new Product()
        {
            Maker = "HP",
            Model = "123",
            Type = "PC"
        };
        db.Products.Add(hp123);
        Pc pc1 = new Pc()
        {
            Product = hp123,
            Price = 100,
            Ram = 32,
            Speed = 10
        };
        db.Pcs.Add(pc1);
        
        db.SaveChanges();
    }
}