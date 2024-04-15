using System;
using System.Collections.Generic;
using System.ComponentModel;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace EFMongo.Models
{
  public class Book
  {
    [BsonId]
    [BsonRepresentation(BsonType.ObjectId)]
    public string Id { get; set; }

    [BsonElement("Name")]
    public string BookName { get; set; }

    [BsonElement("Price")]
    public decimal Price { get; set; }

    [BsonElement("Category")]
    public string Category { get; set; }

    [BsonElement("Author")]
    public string Author { get; set; }

    public int Pages { get; set; }

    public DateTime Published { get; set; }

    public String[] Formats { get; set; }

    public override string ToString()
    {
      return "Book(" +
          "Id: " + Id + "," +
          "BookName: " + BookName + "," +
          "Price: " + Price + "," +
          "Category: " + Category + "," +
          "Author: " + Author + "," +
          "Published: " + Published + "," +
          "Pages: " + Pages +
          ")";
    }

  }
}