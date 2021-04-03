use master
create database QLyTiSoTranDau
go
use QLyTiSoTranDau

create table ThongTinKH(
	HoTen nvarchar(100),
	NamSinh int,
	Sdt char(10),
	Username nvarchar(50),
	Pass nvarchar(50)
)

insert into ThongTinKH(Hoten,NamSinh,Sdt,Username,Pass)
values (N'Bùi Ngọc Chính', '2001', '0977739628', 'buingocchinh321', '016688')

create table BangTiSo(
	MatchCode char(9),
	Home nvarchar(100),
	HomeIcon varbinary(MAX),
	Away nvarchar(100),
	AwayIcon varbinary(MAX),
	HomeGoals char(3),
	AwayGoals char(3)
)

create table ChiTietTranDau(
	MatchCode char(9),
	MatchTime nvarchar(10),
	Team1 nvarchar(50),
	Team2 nvarchar(50),
	MatchEvent nvarchar(100)
)
