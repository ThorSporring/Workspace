using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using LibraryModelUsingEF.db.model;
using Microsoft.EntityFrameworkCore;

namespace LibraryModelUsingEF.db
{
    public class MyDbContext : DbContext
    {
        private const string DbName = "LibraryModelUsingEF";
        private const string ConnectionString = $"Data Source=localhost;Initial Catalog={DbName};User ID=SA;Password=<123123>;Connect Timeout=30;Encrypt=False;Trust Server Certificate=False;Application Intent=ReadWrite;Multi Subnet Failover=False";

        internal DbSet<Author> Authors{ get; set; }
        internal DbSet<Book> Books { get; set; }
        internal DbSet<Loaner> Loaners { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder options)
            => options.UseSqlServer(ConnectionString);
    }
}
