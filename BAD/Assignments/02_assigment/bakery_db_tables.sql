USE master;
-- FOR THIS APPLICATION, ALWAYS CREATE A NEW DATABASE, THIS IS NOT RECOMMENDED IF IT SHOULD BE USED 
DROP DATABASE IF EXISTS Bakery_assignment2_db;

-- Create the database
CREATE DATABASE Bakery_assignment2_db;

-- Use the database
USE Bakery_assignment2_db;

-- Orders Table
CREATE TABLE Orders(
    OrderId INT PRIMARY KEY,
    DeliveryDate DATE,
    DeliveryPlace VARCHAR(255),
    Supermarket VARCHAR(255)
);

-- Baked Good Table
CREATE TABLE BakedGood (
    BakedGoodName VARCHAR(255) PRIMARY KEY
);

-- Order Item Table
CREATE TABLE OrderItem (
    OrderItemId INT PRIMARY KEY,
    Quantity INT,
    OrderId INT FOREIGN KEY REFERENCES Orders(OrderId),
    BakedGoodName VARCHAR(255) FOREIGN KEY REFERENCES BakedGood(BakedGoodName)
);

-- Ingredient Table
CREATE TABLE Ingredient (
    IngredientId INT PRIMARY KEY,
    IngredientName VARCHAR(255) NOT NULL
);

-- Recipe Table
CREATE TABLE Recipe (
    RecipeId INT PRIMARY KEY,
    BakedGoodName VARCHAR(255) FOREIGN KEY REFERENCES BakedGood(BakedGoodName)
);

-- RecipeIngredient Table (Links Recipe to Ingredient)
CREATE TABLE RecipeIngredient (
    RecipeId INT,
    IngredientId INT,
    Quantity INT,
    PRIMARY KEY (RecipeId, IngredientId),
    FOREIGN KEY (RecipeId) REFERENCES Recipe(RecipeId),
    FOREIGN KEY (IngredientId) REFERENCES Ingredient(IngredientId)
);

-- Batch Table
CREATE TABLE Batch (
    BatchNumber INT PRIMARY KEY,
    AmountMade INT,
    StartTime DATETIME,
    FinishTime DATETIME,
    Delay INT,
    OrderId INT FOREIGN KEY REFERENCES Orders(OrderId),
    BakedGoodName VARCHAR(255) FOREIGN KEY REFERENCES BakedGood(BakedGoodName),
    QuantityRequested INT -- This is the quantity requested for this batch in the order
);

-- Stock Table
CREATE TABLE Stock (
    StockId INT PRIMARY KEY,
    Ingredient VARCHAR(255),
    Quantity INT
);

-- Packet Table
CREATE TABLE Packet (
    Route VARCHAR(255),
    TrackingId INT PRIMARY KEY,
    OrderId INT FOREIGN KEY REFERENCES Orders(OrderId)
);

-- Ensuring Availability on Many Batches (using a junction table)
CREATE TABLE StockBatch (
    StockId INT,
    BatchNumber INT,
    PRIMARY KEY (StockId, BatchNumber),
    FOREIGN KEY (StockId) REFERENCES Stock(StockId),
    FOREIGN KEY (BatchNumber) REFERENCES Batch(BatchNumber)
);