﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LibraryModelUsingEF.db.model
{
    internal class Loaner
    {
        public int LoanerId { get; set; }

        public string Name { get; set; }
        public string Address { get; set; }
        public List<Book> Books { get; set; } = new();
    }
}
