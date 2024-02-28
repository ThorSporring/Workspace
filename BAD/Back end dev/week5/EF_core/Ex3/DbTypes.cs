
namespace Ex3
{
    public class Car()
    {// CarId, Brand (string), ProductionYear
        public int CarId { get; set; }
        public string Brand { get; set; }
        public int ProductionYear { get; set; }

        public ICollection<Person> Persons { get; set; }
    }

    public class Person()
    {
        public int PersonId { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Adress { get; set; }
        public ICollection<Car> Cars { get; set; }

    }
    
}
