USE [Electronics]
GO
/****** Object:  Table [dbo].[Laptop]    Script Date: 19-02-2021 07:27:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Laptop](
	[model] [nvarchar](128) NULL,
	[speed] [decimal](10, 2) NULL,
	[ram] [int] NULL,
	[hd] [int] NULL,
	[screen] [decimal](10, 2) NULL,
	[price] [decimal](10, 2) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PC]    Script Date: 19-02-2021 07:27:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PC](
	[model] [nvarchar](128) NULL,
	[speed] [decimal](10, 2) NULL,
	[ram] [int] NULL,
	[hd] [int] NULL,
	[price] [decimal](10, 2) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Printer]    Script Date: 19-02-2021 07:27:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Printer](
	[model] [nvarchar](128) NULL,
	[color] [bit] NULL,
	[type] [nvarchar](32) NULL,
	[price] [decimal](10, 2) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Product]    Script Date: 19-02-2021 07:27:19 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Product](
	[maker] [nvarchar](128) NOT NULL,
	[model] [nvarchar](128) NOT NULL,
	[type] [nvarchar](7) NULL,
PRIMARY KEY CLUSTERED 
(
	[maker] ASC,
	[model] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[model] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Laptop]  WITH CHECK ADD FOREIGN KEY([model])
REFERENCES [dbo].[Product] ([model])
GO
ALTER TABLE [dbo].[PC]  WITH CHECK ADD FOREIGN KEY([model])
REFERENCES [dbo].[Product] ([model])
GO
ALTER TABLE [dbo].[Printer]  WITH CHECK ADD FOREIGN KEY([model])
REFERENCES [dbo].[Product] ([model])
GO
ALTER TABLE [dbo].[Laptop]  WITH CHECK ADD  CONSTRAINT [laptop_screen_hd_price] CHECK  (([Screen]<(15) AND [hd]>(250) AND [PRICE]>(1000.0) OR [PRICE]<(1000.0)))
GO
ALTER TABLE [dbo].[Laptop] CHECK CONSTRAINT [laptop_screen_hd_price]
GO
ALTER TABLE [dbo].[Laptop]  WITH CHECK ADD  CONSTRAINT [speed_gt_2] CHECK  (([speed]>(2.0)))
GO
ALTER TABLE [dbo].[Laptop] CHECK CONSTRAINT [speed_gt_2]
GO
ALTER TABLE [dbo].[PC]  WITH CHECK ADD  CONSTRAINT [pc_speed_price] CHECK  (([speed]<(2.0) AND [price]<(600.0) OR [speed]>(2.0)))
GO
ALTER TABLE [dbo].[PC] CHECK CONSTRAINT [pc_speed_price]
GO
ALTER TABLE [dbo].[Printer]  WITH CHECK ADD  CONSTRAINT [printer_type_is] CHECK  (([type]='bubble-jet' OR [type]='ink-jet' OR [type]='laser'))
GO
ALTER TABLE [dbo].[Printer] CHECK CONSTRAINT [printer_type_is]
GO
ALTER TABLE [dbo].[Product]  WITH CHECK ADD  CONSTRAINT [product_type_is] CHECK  (([type]='printer' OR [type]='laptop' OR [type]='pc'))
GO
ALTER TABLE [dbo].[Product] CHECK CONSTRAINT [product_type_is]
GO
