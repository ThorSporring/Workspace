using Asp.Versioning;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using MyBGList.Models;

namespace MyBGList.Controllers.v3
{
    [Route("v{version:apiVersion}/[controller]")]
    [ApiController]
    [ApiVersion("3.0")]
    [EnableCors("AnyOrigin_GetOnly")]
    [ResponseCache(NoStore = true)]
    public class CodeOnDemandController : ControllerBase
    {

        [HttpGet("Test2/{minutesToAdd}")]
        public ContentResult Test2(int? minutesToAdd)
        {
            var content = "";
            if(minutesToAdd.HasValue)
             {
                content = "<script>" +
                "window.alert('Your client supports JavaScript!" +
                "\\r\\n\\r\\n" +
                $"Server time (UTC): {DateTime.UtcNow.AddMinutes((double)minutesToAdd).ToString("o")}" +
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