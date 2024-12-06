-- Lil skrippy to sort the rules by the right hand column, then the left.
set nocount, xact_abort on
drop table if exists #Rules
create table #Rules
(
    Before int,
	After int
)

insert into #Rules select 47,53
insert into #Rules select 97,13
insert into #Rules select 97,61
insert into #Rules select 97,47
insert into #Rules select 75,29
insert into #Rules select 61,13
insert into #Rules select 75,53
insert into #Rules select 29,13
insert into #Rules select 97,29
insert into #Rules select 53,29
insert into #Rules select 61,53
insert into #Rules select 97,53
insert into #Rules select 61,29
insert into #Rules select 47,13
insert into #Rules select 75,47
insert into #Rules select 97,75
insert into #Rules select 47,61
insert into #Rules select 75,61
insert into #Rules select 47,29
insert into #Rules select 75,13
insert into #Rules select 53,13

select concat(Before, '|', After)
from #Rules
order by After, Before