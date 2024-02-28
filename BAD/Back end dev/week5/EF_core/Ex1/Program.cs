// See https://aka.ms/new-console-template for more information

using Ex1;
using Microsoft.EntityFrameworkCore;

public class CFG()
{
    private static void Main()
    {
        using var db = new MyDbContext();
        // Note: This sample requires the database to be created before running.

        // Create
        Console.WriteLine("Inserting two new blogs");
        db.Blogs.Add(new Blog { Url = "http://blogs.msdn.com/adonet" });
        db.Blogs.Add(new Blog { Url = "http://www.youtube.com" });
        db.SaveChanges();

        // Read
        Console.WriteLine("Querying for a blog");
        var blog = db.Blogs
            .OrderBy(b => b.BlogId)
            .First();
        Console.WriteLine($"BlogId: {blog.BlogId} \turl:{blog.Url}");

        blog = db.Blogs
            .OrderBy(b => b.BlogId)
            .Last();
        Console.WriteLine($"BlogId: {blog.BlogId} \turl:{blog.Url}");

        // Update
        Console.WriteLine("Updating the blog and adding a post");
        blog.Url = "https://devblogs.microsoft.com/dotnet"; 
        blog.Posts.Add(
            new Post { Title = "Hello World", Content = "I wrote an app using EF Core!" });
        db.SaveChanges();
            
        //Delete
        Console.WriteLine("Delete all blogs");
        var allBlogs = db.Blogs.Include(a => a.Posts).ToList();
        foreach(var b in allBlogs)
        {
            db.Remove(b);
            Console.WriteLine($"Removed BlogId: {b.BlogId}, \turl: {b.Url}");
            db.SaveChanges();
            
        }
    }
}