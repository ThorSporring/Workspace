using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;

namespace MyBGList.DTO
{
    public class DomainDTO : IValidatableObject
    {
        [Required]
        public int Id { get; set; }

        [RegularExpression(@"^[a-zA-Z]{1,40}$", ErrorMessage = "Value must contain only letters (no spaces, digits, or other chars)")]
        public string? Name { get; set; }

        public IEnumerable<ValidationResult> Validate(ValidationContext validationContext)
        {
            var results = new List<ValidationResult>();

            if(Name != "WarGames")
            {
                results.Add(new ValidationResult(errorMessage: "Name values must match an allowed Domain."));
            }
            if(Id != 3)
            {
                results.Add(new ValidationResult(errorMessage: "Id values must match an allowed Domain."));
            }

            return results;
        }
    }
}
