USE [Movies]
GO
/****** Object:  Table [dbo].[movieExec]    Script Date: 19-02-2021 07:29:46 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[movieExec](
	[name] [nvarchar](255) NULL,
	[address] [nvarchar](255) NULL,
	[cert] [int] NOT NULL,
	[netWorth] [decimal](10, 2) NULL,
PRIMARY KEY CLUSTERED 
(
	[cert] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[movies]    Script Date: 19-02-2021 07:29:46 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[movies](
	[title] [nvarchar](124) NOT NULL,
	[year] [int] NOT NULL,
	[lenght] [int] NULL,
	[genre] [nvarchar](255) NULL,
	[studioName] [nvarchar](255) NULL,
	[producerC] [int] NULL,
 CONSTRAINT [PK_title_year] PRIMARY KEY CLUSTERED 
(
	[title] ASC,
	[year] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[movieStar]    Script Date: 19-02-2021 07:29:46 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[movieStar](
	[name] [nvarchar](255) NOT NULL,
	[address] [nvarchar](255) NULL,
	[gender] [nvarchar](1) NULL,
	[birthday] [date] NULL,
PRIMARY KEY CLUSTERED 
(
	[name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[starsIn]    Script Date: 19-02-2021 07:29:46 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[starsIn](
	[movieTitle] [nvarchar](124) NOT NULL,
	[movieYear] [int] NOT NULL,
	[movieStarName] [nvarchar](255) NOT NULL,
 CONSTRAINT [PK_mt_my_msn] PRIMARY KEY CLUSTERED 
(
	[movieTitle] ASC,
	[movieYear] ASC,
	[movieStarName] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Studio]    Script Date: 19-02-2021 07:29:46 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Studio](
	[name] [nvarchar](255) NOT NULL,
	[address] [nvarchar](255) NULL,
	[presC] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[movies]  WITH CHECK ADD  CONSTRAINT [FK_exec] FOREIGN KEY([producerC])
REFERENCES [dbo].[movieExec] ([cert])
GO
ALTER TABLE [dbo].[movies] CHECK CONSTRAINT [FK_exec]
GO
ALTER TABLE [dbo].[starsIn]  WITH CHECK ADD FOREIGN KEY([movieTitle], [movieYear])
REFERENCES [dbo].[movies] ([title], [year])
GO
ALTER TABLE [dbo].[starsIn]  WITH CHECK ADD FOREIGN KEY([movieStarName])
REFERENCES [dbo].[movieStar] ([name])
GO
ALTER TABLE [dbo].[movieStar]  WITH CHECK ADD  CONSTRAINT [gender] CHECK  (([gender]='m' OR [gender]='f'))
GO
ALTER TABLE [dbo].[movieStar] CHECK CONSTRAINT [gender]
GO
