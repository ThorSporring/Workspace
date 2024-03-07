// See https://aka.ms/new-console-template for more information

using LibraryModelUsingEF.db;
using LibraryModelUsingEF.db.model;
using Microsoft.EntityFrameworkCore;
using System.Security.Cryptography;

using (var db = new MyDbContext())
{
    SeedDb(db);

    var aId = db.Authors.Select(a => a.AuthorId).First();
    var lId = db.Loaners.Select(l => l.LoanerId).First();

    Console.WriteLine($"PrintAllBooksByAuthorId for id {aId}:");
    PrintAllBooksByAuthorId(db,aId);
    Console.WriteLine();

    Console.WriteLine($"PrintAllBooksByLoanerId for id {lId}:");
    PrintAllBooksByLoanerId(db, lId);

    Console.WriteLine();

    Console.WriteLine($"PrintMostLoanedBook:");
    PrintMostLoanedBook(db);
    Console.WriteLine();

    Console.WriteLine($"PrintLeastLoanedBook:");
    PrintLeastLoanedBook(db);
    Console.WriteLine();

    ClearData(db);
}



void PrintAllBooksByAuthorId(MyDbContext db, int aId)
{
    var books = db.Authors.Include(a=>a.Books).First(a=>a.AuthorId==aId).Books;
    books.ForEach(Console.WriteLine);
}

void PrintAllBooksByLoanerId(MyDbContext db, int lId)
{
    var books = db.Loaners.Include(l => l.Books).First(l => l.LoanerId == lId).Books;
    books.ForEach(Console.WriteLine);
}

void PrintMostLoanedBook(MyDbContext db)
{
    int maxLoan = db.Books.Max(b => b.Loaned);
    var books = db.Books.Where(b => b.Loaned == maxLoan).ToList();

    books.ForEach(Console.WriteLine);
}

void PrintLeastLoanedBook(MyDbContext db)
{
    int minLoan = db.Books.Min(b => b.Loaned);
    var books = db.Books.Where(b => b.Loaned == minLoan).ToList();

    books.ForEach(Console.WriteLine);
}

void SeedDb(MyDbContext db)
{
    var a1 = new Author { Name = "Rowling" };
    var a2 = new Author { Name = "Toby Teorey" };
    var a3 = new Author { Name = "Sam Lightstone" };
    var a4 = new Author { Name = "Tom Nadeau" };

    var b1 = new Book { Title = "Database Modeling and Design", Count = 30,Genre = "professional literature", NumOfPages = 100, Price = 35.5, PublicationDate = new DateTime(2024, 03, 04) };
    var b2 = new Book { Title = "Database entityFramework", Count = 10,Genre = "professional literature", NumOfPages = 100, Price = 35.5, PublicationDate = new DateTime(2024, 03, 04) };
    var b3 = new Book { Title = "My Database and me", Count = 50, Genre = "Bio", NumOfPages = 100, Price = 35.5, PublicationDate = new DateTime(2024, 03, 04) };
    var b4 = new Book { Title = "How to make dragon out of Databases", Count = 5, Genre = "Fantasy", NumOfPages = 100, Price = 35.5, PublicationDate = new DateTime(2024, 03, 04) };

    var l1 = new Loaner { Name = "James Ragnarson", Address = "by the mountain" };
    var l2 = new Loaner { Name = "Remi Ragnarson", Address = "by the mountain" };
    var l3 = new Loaner { Name = "Larry Erickson", Address = "London" };
    var l4 = new Loaner { Name = "Henry Stone", Address = "Randersvej 15, Denmark" };
    var l5 = new Loaner { Name = "Sara Clarkson", Address = "Tatooine" };
    var l6 = new Loaner { Name = "Sami Samson", Address = "the desert some where" };

    b1.Authors.Add(a2);
    b1.Authors.Add(a3);
    b1.Authors.Add(a4);
    b1.LoanBook(l1);
    b1.LoanBook(l2);
    b1.LoanBook(l3);
    b1.LoanBook(l4);
    b1.LoanBook(l5);
    b1.LoanBook(l6);
    
    b2.Authors.Add(a2);
    b2.LoanBook(l3);
    b2.LoanBook(l5);

    b2.Authors.Add(a3);
    b2.LoanBook(l6);

    b3.Authors.Add(a4);
    b3.LoanBook(l2);

    b4.Authors.Add(a1);
    b4.Authors.Add(a2);
    b4.LoanBook(l1);

    b4.LoanBook(l2);
    b4.LoanBook(l3);

    db.Add(b1);
    db.Add(b2);
    db.Add(b3);
    db.Add(b4);
    db.SaveChanges();
}

void ClearData(MyDbContext db)
{
    var authers = db.Authors.ToList();
    var books = db.Books.ToList();
    var loaners = db.Loaners.ToList();

    db.RemoveRange(authers);
    db.RemoveRange(books);
    db.RemoveRange(loaners);
    db.SaveChanges();
}

