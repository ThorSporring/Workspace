using Asp.Versioning;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using MyBGList.Models;
using MyBGList_ApiVersion.DTO.v2;

namespace MyBGList.Controllers.v2
{
    [Route("v{version:apiVersion}/[controller]")]
    [ApiController]
    [ApiVersion("2.0")]
    [EnableCors("AnyOrigin_GetOnly")]
    [ResponseCache(NoStore = true)]
    public class CodeOnDemandController : ControllerBase
    {

        [HttpGet("Test")]
        public ContentResult Test()
        {
            var content = "<script>" +
        "window.alert('Your client supports JavaScript!" +
        "\\r\\n\\r\\n" +
        $"Server time (UTC): {DateTime.UtcNow.ToString("o")}" +
        "\\r\\n" +
        "Client time (UTC): ' + new Date().toISOString());" +
        "</script>" +
        "<noscript>Your client does not support JavaScript</noscript>";
        
            return Content(content ,"text/html");
        }

        [HttpGet("Test2/{addMinutes}")]
        public ContentResult Test2(int? addMinutes)
        {
            var content = "";
            if(addMinutes.HasValue)
             {
                content = "<script>" +
                "window.alert('Your client supports JavaScript!" +
                "\\r\\n\\r\\n" +
                $"Server time (UTC): {DateTime.UtcNow.AddMinutes((double)addMinutes).ToString("o")}" +
                "\\r\\n" +
                $"Client time (UTC): ' + new Date().toISOString());" +
                "</script>" +
                "<noscript>Your client does not support JavaScript</noscript>";
             }
             else{
                content = "<script>" +
                "window.alert('Your client supports JavaScript!" +
                "\\r\\n\\r\\n" +
                $"Server time (UTC): {DateTime.UtcNow.ToString("o")}" +
                "\\r\\n" +
                "Client time (UTC): ' + new Date().toISOString());" +
                "</script>" +
                "<noscript>Your client does not support JavaScript</noscript>";
             }

            

            return Content(content, "text/html");

        }
    }
}