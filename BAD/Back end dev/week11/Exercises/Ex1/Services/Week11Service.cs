using Ex1.Models;
using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ex1.Services
{
    public class Week11Service
    {

        private IMongoCollection<Pet> _pets;
        private IMongoCollection<Person> _persons;
        
        private readonly string _connectionString = "mongodb://localhost:32768/Week11";
        private readonly string _database = "Week11";
        private readonly string _personsCollection = "Persons";
        private readonly string _petsCollections = "Pets";

        public Week11Service()
        {
            var client = new MongoClient(_connectionString);
            var database = client.GetDatabase(_database);
            _persons = database.GetCollection<Person>(_personsCollection);
            _pets = database.GetCollection<Pet>(_petsCollections);
            Seed();
        }

        public void Seed()
        {
            var people = new List<Person>
            {
                new Person { Name = "John", Address = "123 Main St", Owns = new List<string> { "Fluffy", "Lucy" } },
                new Person { Name = "Alice", Address = "456 Elm St", Owns = new List<string> { "Charlie" } },
                new Person { Name = "Bob", Address = "789 Oak St" },
                new Person { Name = "Melissa", Address = "76 Water St", Owns = new List<string>{"Carlo, Juicy, Tucker"}}
            };
            var pets = new List<Pet>
            {
                new Pet { Name = "Fluffy", Years = 12, Race = "Border Collie", Weight = 12.4, Owner = "John"},
                new Pet { Name = "Lucy", Years = 1, Race = "Rottweiler", Weight = 11, Owner = "John"},
                new Pet { Name = "Charlie", Years = 4, Race = "Chiuahahaua", Weight = 5, Owner = "Alice"},
                new Pet { Name = "Carlo", Years = 3, Race = "Labrador", Weight = 15, Owner = "Melissa"},
                new Pet { Name = "Juicy", Years = 6, Race = "Poodle", Weight = 9, Owner = "Melissa"},
                new Pet { Name = "Tucker", Years = 1, Race = "Shitzu", Weight = 3, Owner = "Melissa"},
                new Pet { Name = "Wacko", Years = 6, Race = "Shitzu", Weight = 5},
                new Pet { Name = "Bobo", Years = 5, Race = "Shitzu", Weight = 1},
                new Pet { Name = "Smutzi", Years = 10, Race = "Shitzu", Weight = 2}

            };

            if (!_persons.AsQueryable().Any())
            {
                _persons.InsertMany(people);
                Console.WriteLine("Sample data inserted into Persons collection ");
            }
            if (!_pets.AsQueryable().Any()) 
            {
                _pets.InsertMany(pets);
                Console.WriteLine("Sample data inserted into Pets collections");
            }
        }

        public 
        

    }
}

