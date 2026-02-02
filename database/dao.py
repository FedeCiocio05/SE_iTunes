from database.DB_connect import DBConnect
from model.album import Album

class DAO:
    @staticmethod
    def get_album_nodes(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT a.id, a.title, a.artist_id, SUM(t.milliseconds/60000) as duration
                    FROM album a, track t
                    WHERE a.id = t.album_id
                    GROUP BY a.id, a.title, a.artist_id
                    HAVING duration >= %s"""

        cursor.execute(query, (durata,))

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_edges(durata):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """ SELECT al1.id as a1,al2.id as a2
                    FROM album al1,album al2,track t1,track t2,playlist_track p1,playlist_track p2
                    WHERE al1.id = t1.album_id AND t1.id = p1.track_id
                        AND al2.id = t2.album_id AND t2.id = p2.track_id
                        AND p1.playlist_id = p2.playlist_id
                        AND al1.id > al2.id
                        AND al1.id in (SELECT a.id
                                            FROM album a,track t
                                            WHERE t.album_id = a.id
                                            GROUP BY a.id,a.title,a.artist_id
                                            HAVING SUM(t.milliseconds)/60000 > %s)
                        AND al2.id in (SELCT a.id
                                            FROM album a,track t
                                            WHERE t.album_id = a.id
                                            GROUP BY a.id,a.title,a.artist_id
                                            HAVING SUM(t.milliseconds)/60000 > %s)
                        GROUP BY al1.id,al2.id"""

        cursor.execute(query, (durata, durata))

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

