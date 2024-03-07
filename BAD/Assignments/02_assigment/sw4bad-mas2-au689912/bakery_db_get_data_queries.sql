USE Bakery_assignment2_db;
GO

-- Get the current stock
SELECT * FROM Stock;
GO

-- Get the adress for order 1
SELECT DeliveryPlace FROM Orders WHERE OrderId = 1;
GO

-- Get the list of baked goods in order 1
SELECT BakedGoodName, Quantity
FROM OrderItem
WHERE OrderId = 1;
GO

-- Get the ingredients for batch number 101
SELECT ri.IngredientId, i.IngredientName, ri.Quantity
FROM RecipeIngredient ri
JOIN Recipe r ON ri.RecipeId = r.RecipeId
JOIN Batch b ON r.BakedGoodName = b.BakedGoodName
JOIN Ingredient i ON ri.IngredientId = i.IngredientId
WHERE b.BatchNumber = 101;

-- Get the tracking id for order 1
SELECT TrackingId
FROM Packet
WHERE OrderId = 1;
GO

-- Produce a table containing the quantities of each of the baking goods in 
-- all the orders received so far (NB: First column is in Ascending order)
SELECT BakedGoodName, SUM(Quantity) AS TotalQuantity
FROM OrderItem
GROUP BY BakedGoodName
ORDER BY BakedGoodName ASC;
GO

-- Get the average delay for all the batches
SELECT AVG(Delay) AS AverageDelay
FROM Batch;
GO