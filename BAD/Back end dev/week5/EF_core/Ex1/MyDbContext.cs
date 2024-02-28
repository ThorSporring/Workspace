using Microsoft.EntityFrameworkCore;

namespace Ex1;

public class MyDbContext : DbContext
{
    private const string DbName = "week5_exercises";
    private const string ConnectionString = $"Data Source=localhost;Initial Catalog={DbName};User ID=SA;Password=<123123>;Connect Timeout=30;Encrypt=False;Trust Server Certificate=False;Application Intent=ReadWrite;Multi Subnet Failover=False";
 
    public DbSet<Blog> Blogs { get; set; }
    public DbSet<Post> Posts { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder options)
        => options.UseSqlServer(ConnectionString);
    //recheck connectionString if issue connecting to db
    //can reuse connection string from week 3 using your new database
}