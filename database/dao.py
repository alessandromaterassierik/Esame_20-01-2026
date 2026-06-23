from database.DB_connect import DBConnect

class DAO:

    @staticmethod
    def get_all_artists():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT *
                FROM artist a"""

        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_num_albums(n_alb):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ with num_album as (select al.artist_id, count(*) as n_alb  from album al group by artist_id),
                    
                    artist_val as (select * from num_album aa 
                    join artist a on a.id = aa.artist_id 
                    where n_alb >= %s),
                    
                    art_gen as (select distinct a.artist_id, ar.name, t.genre_id from album a join track t on a.id = t.album_id 
                    join artist ar on ar.id=a.artist_id),
                    
                    art_art as (select distinct ag1.artist_id as art1, ag2.artist_id as art2, ag1.name as name1, ag2.name as name2, count(*) as generi_com 
                    from art_gen ag1, art_gen ag2 
                    where ag1.artist_id > ag2.artist_id and ag1.genre_id = ag2.genre_id
                    group by ag1.artist_id, ag2.artist_id)
                    
                    select  aa.art1, aa.art2 , aa.name1, aa.name2, generi_com
                    from art_art aa
                    where aa.art1 in (select av1.id from artist_val av1 ) and aa.art2 in (select av2.id from artist_val av2 )
                    group by aa.art1, aa.art2 """

        cursor.execute(query, (n_alb,))
        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_albums_filtered(n_alb, d_min):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """with num_album as (select al.artist_id, count(*) as n_alb  from album al group by artist_id),

artist_val as (select * from num_album aa 
join artist a on a.id = aa.artist_id 
where n_alb >= %s),

album_filtered as (select album_id from track t where t.milliseconds/ 60000 >= %s),

art_gen as (select distinct a.artist_id, ar.name, t.genre_id from album a join track t on a.id = t.album_id 
join artist ar on ar.id=a.artist_id
where t.album_id in (select af.album_id from album_filtered af)),

art_art as (select distinct ag1.artist_id as art1, ag2.artist_id as art2, ag1.name as name1, ag2.name as name2, count(*) as generi_com 
from art_gen ag1, art_gen ag2 
where ag1.artist_id > ag2.artist_id and ag1.genre_id = ag2.genre_id
group by ag1.artist_id, ag2.artist_id)


select  aa.art1, aa.art2 , aa.name1, aa.name2, generi_com
from art_art aa
where aa.art1 in (select av1.id from artist_val av1 ) and aa.art2 in (select av2.id from artist_val av2 )
group by aa.art1, aa.art2"""

        cursor.execute(query, (n_alb,d_min,))
        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result