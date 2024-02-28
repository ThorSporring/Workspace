using System.Reflection.Emit;

namespace EX2
{
    public class Product
    {
        public int ProductId { get; set; }
        public string Maker { get; set; }
        public string Model { get; set; }
        public string Type { get; set; }

        public override string ToString()
        {
            return $"ProductId: {ProductId}, Maker: {Maker}, Model: {Model}, Type: {Type}";
        }
    }

    public class Pc
    {
        public int PcId { get; set; }
        public int Speed { get; set; } // GHz
        public int Ram { get; set; }   // GB
        public int Price { get; set; } // Dollars

        public int ProductId { get; set; }
        public Product Product { get; set; }

        public override string ToString()
        {
            return $"PcId: {PcId}, Speed: {Speed} GHz, Ram: {Ram} GB, Price: ${Price}, {Product}";
        }
    }

    public class Laptop
    {
        public int LaptopId { get; set; }
        public int Speed { get; set; } // GHz
        public int Ram { get; set; }   // GB
        public int Price { get; set; } // Dollars

        public int ProductId { get; set; }
        public Product Product { get; set; }

        public override string ToString()
        {
            return $"LaptopId: {LaptopId}, Speed: {Speed} GHz, Ram: {Ram} GB, Price: ${Price}, {Product}";
        }
    }

    public class Printer
    {
        public int PrinterId { get; set; }
        public string Color { get; set; }
        public string Type { get; set; }
        public int Price { get; set; }

        public int ProductId { get; set; }
        public Product Product { get; set; }

        public override string ToString()
        {
            return $"PrinterId: {PrinterId}, Color: {Color}, Type: {Type}, Price: ${Price}, {Product}";
        }
    }
}

