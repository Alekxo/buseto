package com.example.krrish.mymap;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import org.osmdroid.api.IMapController;
import org.osmdroid.tileprovider.tilesource.TileSourceFactory;
import org.osmdroid.util.GeoPoint;
import org.osmdroid.views.MapView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);

        MapView mapView = (MapView) findViewById(R.id.map_view);
        mapView.setTileSource(TileSourceFactory.PUBLIC_TRANSPORT);
        mapView.setBuiltInZoomControls(true);
        mapView.setMultiTouchControls(true);

        IMapController mapController = mapView.getController();
        mapController.setZoom(9);
        GeoPoint location = new GeoPoint(27.7166667,85.3166667);
        mapController.setCenter(location);
    }

    public void onResume(){
        super.onResume();
    }
}
