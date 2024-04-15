using MongoDB.Bson.Serialization.Attributes;
using MongoDB.Bson;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ex1.Models;

[BsonIgnoreExtraElements]
public class Pet
{

    [BsonId]
    [BsonRepresentation(BsonType.ObjectId)]
    public string Id { get; set; }

    [BsonElement("Name")]
    public string Name = "";

    [BsonElement("Years")]
    public int Years = 0;

    [BsonElement("Race")]
    public string Race = "";

    [BsonElement("Weight")]

    public double Weight = 0.0;

    [BsonElement("Owner")]

    public String Owner = "";
}

