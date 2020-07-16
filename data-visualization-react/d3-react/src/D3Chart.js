import * as d3 from 'd3';//not efficient way

//Adding multiple svgs at a time can be done either
//use for loops
/*data.forEach((d, i) => {    
            svg.append("rect")
            .attr("x", i * 100)
            .attr("y",50)
            .attr("width",50)
            .attr("height",d)
            .attr("fill","grey")
        })*/
//use data joins: More efficient
const MARGIN = { TOP: 10, BOTTOM: 50, LEFT: 70, RIGHT: 10}
const WIDTH = 800 - MARGIN.LEFT - MARGIN.RIGHT;
const HEIGHT = 500 - MARGIN.TOP - MARGIN.BOTTOM;

export default class D3Chart {
    constructor(element) {
        const vis = this
        vis.svg = d3.select(element) //this creates a new property on vis object and sets svg to this canvas
            .append("svg")
                .attr("width", WIDTH + MARGIN.LEFT + MARGIN.RIGHT) //svg canvas should be original val
                .attr("height", HEIGHT + MARGIN.TOP + MARGIN.BOTTOM)
            .append("g")
                .attr("transform", `translate(${MARGIN.LEFT}, ${MARGIN.TOP})`)
        
        
        vis.xLabel = vis.svg.append("text")
            .attr("x", WIDTH / 2)
            .attr("y", HEIGHT + 50)
            .attr("text-anchor", "middle")

        vis.svg.append("text")
            .attr("x", -(HEIGHT / 2))
            .attr("y", -50)
            .attr("text-anchor", "middle")
            .text("Height in cm")
            .attr("transform", "rotate(-90)")
        
        //they are called inside update function
        //add agroups to constructor method just once
        //whenever these  changed call method recalculate the axis
        vis.xAxisGroup = vis.svg.append("g")
            .attr("transform", `translate(0,${HEIGHT})`)
        
        vis.yAxisGroup = vis.svg.append("g")

        //Promise.all for working with multiple sets of data at once
        //Prmise.all allows us to pass multiple promises as an array
        //and work with the results of these promises using a single callback function from a single then method
        //Better approach than nesting different calls to d3.json
        Promise.all([
            d3.json("https://udemy-react-d3.firebaseio.com/tallest_men.json"),
            d3.json("https://udemy-react-d3.firebaseio.com/tallest_women.json")
        ]).then((datasets) => {
            vis.menData = datasets[0]
            vis.womenData = datasets[1]
            vis.update("men")
            //Destructuring
            /*const [men, women] = datasets
            let flag = true

            vis.data = men
            vis.update() //initial interval 1 sec shows data

            d3.interval(() => {
                vis.data = flag ? men : women //ternary operator JS
                vis.update()
                const gender = flag ? "men" : "women"
                vis.xlabel.text(`The world's tallest ${gender}`)
                flag =! flag
            }, 1000)*/
        }) 
    }
    update(gender) {
        const vis = this

        vis.data = (gender == "men" ) ? vis.menData : vis.womenData;
        vis.xLabel.text(`The world's tallest ${gender}`)
       // vis.xLabel.text(`The world's tallest ${gender}`)
        //Scaling
        //Returns a function
        const y = d3.scaleLinear()
            .domain([
                d3.min(vis.data, d => d.height)* 0.95, //0.95 for making the smallest bar visible :) 
                d3.max(vis.data, d => d.height)
            ]) //Max height in our data
            .range([HEIGHT, 0]) //Height of our visualization
            
        const x = d3.scaleBand()
            .domain(vis.data.map(d => d.name))
            .range([0, WIDTH])
            .padding(0.4)

        //Axis generator
        const xAxisCall = d3.axisBottom(x)
        vis.xAxisGroup.transition().duration(500).call(xAxisCall)// Adding the same transtion for axis

        const yAxisCall = d3.axisLeft(y)
        vis.yAxisGroup.transition().duration(500).call(yAxisCall)

        //1. Data JOIN : Tell which array of data we need to associate with the shapes
        const rects = vis.svg.selectAll("rect")
            .data(vis.data)

        //2. Exit
        rects.exit()
            .transition().duration(500)
                .attr("height", 0)
                .attr("y", HEIGHT)
                .remove()

        //3. Update : Works on group selection
        rects.transition().duration(500)
            .attr("x", d => x(d.name))
            .attr("y", d => y(d.height))
            .attr("width", x.bandwidth)
            .attr("height", d => HEIGHT - y(d.height))


        //4. Enter: Virtual selector enter that shows the rectangle on the screen that are contained in the data    
         rects.enter().append("rect")
            .attr("x", d => x(d.name))
            .attr("width", x.bandwidth) //x.bandwidth
            .attr("fill", "green")
            .attr("y", HEIGHT)
            .transition().duration(500)
                .attr("height", d => HEIGHT - y(d.height))
                .attr("y", d => y(d.height))
    }
}