using Asp.Versioning;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using MyBGList.Models;
using MyBGList_ApiVersion.DTO.v2;

namespace MyBGList.Controllers.v2
{
    [Route("v{version:apiVersion}/[controller]")]
    [ApiController]
    [ApiVersion("2.0")]
    public class BoardGamesController : ControllerBase
    {
        private readonly ILogger<BoardGamesController> _logger;
        public BoardGamesController(ILogger<BoardGamesController> logger)
        {
            _logger = logger;
        }

        [HttpGet(Name = "GetBoardGames")]
        [ResponseCache(Location = ResponseCacheLocation.Client, Duration = 120)]
        public RestDTO<BoardGame[]> Get()
        {
            return new RestDTO<BoardGame[]>()
            {
                Items = new[] {
                    new BoardGame()
                    {
                        Id = 1,
                        Name = "Axis & Allies",
                        Year = 1981
                    },
                    new BoardGame()
                    {
                        Id = 2,
                        Name = "Citadels",
                        Year = 2000
                    },
                    new BoardGame()
                    {
                        Id = 3,
                        Name = "Terraforming Mars",
                        Year = 2016
                    }
                },
                Links = new List<MyBGList_ApiVersion.DTO.v1.LinkDTO>
                {
                    new MyBGList_ApiVersion.DTO.v1.LinkDTO(
                        Url.Action(null, "BoardGames", null, Request.Scheme)!,
                        "self",
                        "GET"),
                }
            };
        }
    }
}
