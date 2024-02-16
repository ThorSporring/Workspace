using Asp.Versioning;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using Microsoft.OpenApi.Models;
using MyBGList_ApiVersion.DTO.v1;
using MyBGList_ApiVersion.DTO.v2;
using System;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddCors(options => {
    options.AddDefaultPolicy(cfg => {
        cfg.WithOrigins(builder.Configuration["AllowedOrigins"]);
        cfg.AllowAnyHeader();
        cfg.AllowAnyMethod();
    });
    options.AddPolicy(name: "AnyOrigin",
        cfg => {
            cfg.AllowAnyOrigin();
            cfg.AllowAnyHeader();
            cfg.AllowAnyMethod();
        });
    options.AddPolicy(name: "AnyOrigin_GetOnly",
        cfg => {
            cfg.AllowAnyOrigin();
            cfg.AllowAnyHeader();
            cfg.WithMethods("GET");
        });
});

builder.Services.AddApiVersioning(options =>
{
    //options.ReportApiVersions = true;
    options.ApiVersionReader = new UrlSegmentApiVersionReader();
    options.AssumeDefaultVersionWhenUnspecified = true;
    options.DefaultApiVersion = new ApiVersion(1, 0);
})
.AddMvc() // Brings in MVC Core support
.AddApiExplorer(options =>
{
    options.GroupNameFormat = "'v'VVV";
    options.SubstituteApiVersionInUrl = true;
});

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();

builder.Services.AddSwaggerGen(options => {
    options.SwaggerDoc(
    "v1",
    new OpenApiInfo { Title = "MyBGList", Version = "v1.0" });
    options.SwaggerDoc(
    "v2",
    new OpenApiInfo { Title = "MyBGList", Version = "v2.0" });
    options.SwaggerDoc(
    "v3",
    new OpenApiInfo { Title = "MyBGList", Version = "v3.0" });
});


var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(options => {
        options.SwaggerEndpoint(
        $"/swagger/v1/swagger.json",
        $"MyBGList v1");
        options.SwaggerEndpoint(
        $"/swagger/v2/swagger.json",
        $"MyBGList v2");
        options.SwaggerEndpoint(
        $"/swagger/v3/swagger.json",
        $"MyBGList v3");
    });
}

if (app.Configuration.GetValue<bool>("UseDeveloperExceptionPage"))
    app.UseDeveloperExceptionPage();
else
    app.UseExceptionHandler("/error");

app.UseHttpsRedirection();

app.UseCors();

app.UseAuthorization();

// Minimal API
app.MapGet("/v1/error",
    [ApiVersion("1.0")]
[ApiVersion("2.0")]
[EnableCors("AnyOrigin")]
[ResponseCache(NoStore = true)] () =>
    Results.Problem());

app.MapGet("/v1/error/test",
    [ApiVersion("1.0")]
[ApiVersion("2.0")]
[EnableCors("AnyOrigin")]
[ResponseCache(NoStore = true)] () =>
    { throw new Exception("test"); });

app.MapGet("/v1/cod/test",
    [ApiVersion("1.0")]
[ApiVersion("2.0")]
[EnableCors("AnyOrigin_GetOnly")]
[ResponseCache(NoStore = true)] () =>
    Results.Text("<script>" +
        "window.alert('Your client supports JavaScript!" +
        "\\r\\n\\r\\n" +
        $"Server time (UTC): {DateTime.UtcNow.ToString("o")}" +
        "\\r\\n" +
        "Client time (UTC): ' + new Date().toISOString());" +
        "</script>" +
        "<noscript>Your client does not support JavaScript</noscript>",
        "text/html"));

var demo = app.NewVersionedApi();
var v1 = demo.MapGroup("/demo/v{version:apiVersion}")
    .HasApiVersion(1.0);

v1.MapGet("/", () => "This is a simple demo");

var v2 = demo.MapGroup("/demo/v{version:apiVersion}")
    .HasApiVersion(2.0);
v2.MapGet("/", () => "This is v2");

var v3 = demo.MapGroup("/demo/v{version:apiVersion}")
    .HasApiVersion(3.0);
v3.MapGet("/", () => "This is v3");

// Controllers
app.MapControllers();

app.Run();
