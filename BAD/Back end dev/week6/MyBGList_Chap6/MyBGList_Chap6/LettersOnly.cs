using Microsoft.AspNetCore.Mvc.ModelBinding.Validation;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Text.Json.Serialization;
using System.Text.RegularExpressions;

namespace MyBGList;
public class LettersOnly : ValidationAttribute
{
    public new string ErrorMessage { get; set; } = "Value must contain only letters (no spaces, digits, or other chars)";

    protected override ValidationResult? IsValid(object? value, ValidationContext validationContext)
    {
        if (value != null)
        {
            var valueString = value.ToString();
            if (Regex.IsMatch(valueString, @"^[a-zA-Z]{1,40}$"))
            {  
                return ValidationResult.Success;
            }    
        }
        
        return new ValidationResult(ErrorMessage);
    }
}