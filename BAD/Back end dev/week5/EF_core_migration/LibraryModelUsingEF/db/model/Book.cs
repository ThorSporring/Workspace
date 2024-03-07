using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibraryModelUsingEF.db.model
{
    internal class Book
    {
        public int BookId { get; set; }
        public string Title { get; set; }
        public int Loaned { get; set; }
        public int Count { get; set; }
        public string Genre { get; set; }
        public double Price { get; set; }
        public int NumOfPages { get; set; }
        public DateTime PublicationDate { get; set; }

        public List<Author> Authors { get; set; } = new();
        public List<Loaner> Loaners { get; set; } = new();

        public override string ToString()
        {
            return $"BookId: {BookId},   Title: {Title},   Genre: {Genre},   Count: {Count},   LoanedCount: {Loaned}";
        }

        public bool LoanBook(Loaner l)
        {
            if (FreeBook())
            {
                Loaners.Add(l);
                Loaned++;
            }
            return FreeBook();
        }

        public bool FreeBook() => Loaned < Count;
    }
}
